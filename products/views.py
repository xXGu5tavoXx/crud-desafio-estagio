from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Produto
import json

# --- Funções Auxiliares ---

# Função para serializar um único produto para JSON
def serialize_produto(produto ):
    return {
        'id': produto.id,
        'nome': produto.nome,
        'descricao': produto.descricao,
        'preco': str(produto.preco), # Converte Decimal para string para JSON
        'quantidade': produto.quantidade,
    }

# Função para validar os dados (Requisito 3)
def validate_data(data):
    errors = {}
    
    # Validação do campo nome (não pode estar vazio)
    if not data.get('nome'):
        errors['nome'] = 'O campo nome não pode estar vazio.'

    # Validação do campo preco (deve ser um número positivo)
    try:
        preco = float(data.get('preco'))
        if preco <= 0:
            errors['preco'] = 'O campo preço deve ser um número positivo.'
    except (TypeError, ValueError):
        errors['preco'] = 'O campo preço deve ser um número válido.'
    
    # Validação do campo quantidade (deve ser um número positivo)
    try:
        quantidade = int(data.get('quantidade'))
        if quantidade <= 0:
            errors['quantidade'] = 'O campo quantidade deve ser um número positivo.'
    except (TypeError, ValueError):
        errors['quantidade'] = 'O campo quantidade deve ser um número inteiro válido.'

    return errors

# --- Views da API ---

@csrf_exempt # Permite requisições POST/PUT/DELETE sem token CSRF (para simplificar a API)
def produto_list_create(request):
    # Listar todos os produtos (GET)
    if request.method == 'GET':
        produtos = Produto.objects.all()
        data = [serialize_produto(p) for p in produtos]
        return JsonResponse(data, safe=False)

    # Criar um novo produto (POST)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        errors = validate_data(data)
        if errors:
            return JsonResponse({'errors': errors}, status=400) # Retorna erros de validação

        try:
            produto = Produto.objects.create(
                nome=data['nome'],
                descricao=data.get('descricao', ''),
                preco=data['preco'],
                quantidade=data['quantidade']
            )
            return JsonResponse(serialize_produto(produto), status=201) # 201 Created
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def produto_detail_update_delete(request, pk):
    # Busca o produto ou retorna 404 Not Found
    produto = get_object_or_404(Produto, pk=pk)

    # Exibir os detalhes de um produto específico (GET)
    if request.method == 'GET':
        return JsonResponse(serialize_produto(produto))

    # Atualizar os detalhes de um produto (PUT/PATCH)
    elif request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        # Prepara os dados para validação (usa os dados existentes como fallback)
        update_data = {
            'nome': data.get('nome', produto.nome),
            'descricao': data.get('descricao', produto.descricao),
            'preco': data.get('preco', produto.preco),
            'quantidade': data.get('quantidade', produto.quantidade),
        }

        errors = validate_data(update_data)
        if errors:
            return JsonResponse({'errors': errors}, status=400)

        try:
            # Aplica as alterações e salva
            produto.nome = update_data['nome']
            produto.descricao = update_data['descricao']
            produto.preco = update_data['preco']
            produto.quantidade = update_data['quantidade']
            produto.save()
            return JsonResponse(serialize_produto(produto))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # Excluir um produto (DELETE)
    elif request.method == 'DELETE':
        produto.delete()
        return JsonResponse({'message': 'Produto excluído com sucesso'}, status=204) # 204 No Content

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def produto_search(request):
    # Pesquisa de Produtos pelo nome (GET) (Requisito 4)
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            # Pesquisa parcial (icontains)
            produtos = Produto.objects.filter(nome__icontains=query)
        else:
            # Se a query estiver vazia, retorna todos
            produtos = Produto.objects.all()

        data = [serialize_produto(p) for p in produtos]
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

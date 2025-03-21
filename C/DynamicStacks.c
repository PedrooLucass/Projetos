#include <stdio.h>
#include <stdlib.h>
/*
Ressalva:
 Eu poderia usar obviamente váriaveis globais, ainda mais pra pilha e pro topo da pilha, 
 realmente facilitaria o código e tornaria ele menos reduntante,
 mas particularmente não gosto delas e evitarei ao máximo.
*/

int push(int *vetor, int topo)
{
    int insert;

    printf("O que deseja colocar na pilha? ");
    scanf(" %d", &insert);

    *(vetor + topo) = insert;
    printf("Adicionado com sucesso!\n");
    return ++topo;
}
int pop(int *vetor, int topo)
{
    if (topo == 0)
    {
        printf("Pilha ja esta vazia.\n");
    }
    *(vetor + topo) = 0;
    return --topo;
}
void list(int *vetor, int topo)
{
    int i;

    printf("Aqui esta a lista: \n");
    for(i = 0; i < topo; i++)
    {
        printf("%d - %d\n", i+1, *(vetor+i));
    }
    printf("\n");
}
int peek(int *vetor, int topo)
{
    return *(vetor + (topo - 1));
}
int clear(int *vetor, int topo)
{
    int i, opcao;

    printf("Voce tem certeza que deseja apagar TODOS os elementos da pilha? \nCaso sim, digite 1, caso nao, digite 2.\n");
    scanf(" %d", &opcao);
    if(opcao == 1)
    {
        for(i = topo; i > 0; i--)
        {
            *(vetor + topo) = 0;
        }
        topo = 0;
        printf("Pilha esvaziada.\n");
    }
    return topo;
}
int switchsize(int *vetor, int topo, int tamanho, int tamanhonovo)
{
    /*
    Essa função é um pouco mais confusa então resumirei
    1- aux vai clonar a nossa pilha
    2- a pilha vai receber o novo tamanho
    3- com o if, aux passará novamente os elementos pra pilha principal
    O IF existe para não ter chance de estourar o novo limite da pilha
    */

    int *aux = NULL, i;

    aux = (int*) malloc(sizeof(int) * tamanho);

    for(i = 0; i < tamanho; i++)
    {
        *(aux + i) = *(vetor + i);
    }

    vetor = (int*) malloc(sizeof(int) * tamanhonovo);

    if (tamanho > tamanhonovo)
    {
        for(i = 0; i < tamanhonovo; i++)
        {
            *(vetor + i) = *(aux + i);
        }
        topo = tamanhonovo;
    } else {
        for(i = 0; i < tamanho; i++)
        {
            *(vetor + i) = *(aux + i);
        }
    }
    free(aux);
    return topo;
}
int main()
{
    int opcao, tamanho, topo = 0, *stack = NULL;

    printf("Inicialmente, qual tamanho maximo deseja usar na pilha?\n");
    scanf(" %d", &tamanho);

    stack = (int*) malloc(sizeof(int) * tamanho);

    while (opcao != 8)
    {
        printf("1 - Adicionar elemento (push)\n");
        printf("2 - Remover ultimo elemento (pop)\n");
        printf("3 - Listar toda pilha (list)\n");
        printf("4 - Ultimo elemento adicionado (peek)\n");
        printf("5 - Tamanho atual da pilha (size)\n");
        printf("6 - Limpar toda a pilha (clear)\n");
        printf("7 - Trocar tamanho maximo\n");
        printf("8 - Sair\n");
        printf("Sua opcao: ");
        scanf(" %d", &opcao);
        printf("\n");

        if(opcao == 1)
        {
            if(topo >= tamanho)
            {
                printf("Tamanho maximo atingido, remova ou troque o tamanho maximo da pilha.\n");
            } else {
                topo = push(stack, topo);
            }
        }
        else if(opcao == 2)
        {
            topo = pop(stack, topo);
        }
        else if(opcao == 3)
        {
            list(stack, topo);
        }
        else if(opcao == 4)
        {
            printf("O ultimo valor colocado foi: %d\n", peek(stack, topo));
        }
        else if(opcao == 5)
        {
            printf("O ultimo index usado foi: %d\n", topo);
        }
        else if(opcao == 6)
        {
            topo = clear(stack, topo);
        }
        else if(opcao == 7)
        {
            int tamanhonovo;
            printf("Qual o novo tamanho da pilha? ");
            scanf(" %d", &tamanhonovo);
            topo = switchsize(stack, topo, tamanho, tamanhonovo);
            tamanho = tamanhonovo;
        }
        else if(opcao == 8)
        {
            free(stack);
        } 
        else {
            printf("Numero invalido! Tente novamente.\n");
        }
    }
    return 0; 
}

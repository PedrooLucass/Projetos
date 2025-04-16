#include <stdio.h>

void bubblesort(int *vetor, int tamanho, int *contador)
{
    int i, j, aux;
    for (i = tamanho; i > 0; i--)
    {
        for (j = 0; j < tamanho - 1; j++)
        {
            *(contador) = *(contador) + 1;
            if(*(vetor + j) > *(vetor + j + 1))
            {
                *(contador + 1) = *(contador + 1) + 1;
                aux = *(vetor + j);
                *(vetor + j) = *(vetor + j + 1);
                *(vetor + j + 1) = aux;
            }
        }
    }
}
void selectionsort(int *vetor, int tamanho, int *contador)
{
    int i, j, aux, minimo;
    for (i = 0; i < tamanho; i++)
    {
        minimo = i;
        for (j = 0 + i; j < tamanho; j++)
        {
            *(contador) = *(contador) + 1;
            if(*(vetor + j) < *(vetor + minimo))
            {
                minimo = j;
            }
        }
        *(contador + 1) = *(contador + 1) + 1;
        aux = *(vetor + minimo);
        *(vetor + minimo) = *(vetor + i);
        *(vetor + i) = aux;
    } 
}

int main(void)
{
    int vetor[] = {93, 82, 10, 02, 41, 07, 62, 77, 18, 61, 06, 29};
    int tamanho = 12;
    //int vetor[] = {29, 10, 14, 37, 14};
    //int tamanho = 5;

    int contador[] = {0, 0}; 
    // index 0 é a quantidade de comparações 
    // index 1 é a quantidade de trocas

    int i, opcao;

    printf("Escolha o SORT que sera usado: \n");
    printf("1 - Bubble Sort\n");
    printf("2 - Selection Sort\n");
    printf("Sua opcao: ");
    scanf(" %d", &opcao);

    if(opcao == 1)
    {
        bubblesort(vetor, tamanho, contador);
        printf("Bubble sort feito com sucesso!\n");
    } 
    else if(opcao == 2)
    {
        selectionsort(vetor, tamanho, contador);
        printf("Selection sort feito com sucesso!\n");
    } else {
        printf("Numero invalido.\n");
    }

    printf("Aqui esta o vetor organizado: {");
    for (i = 0; i < tamanho; i++)
    {
        if (i == tamanho - 1)
        {
            printf("%d}\n", *(vetor + i));
        } else {
            printf("%d, ", *(vetor + i));
        }
    }
    printf("Foram usados %d comparacoes e %d trocas de valores.\n", contador[0], contador[1]);
}
#include "lists.h"

/**
 * is_palindrome - entry point
 * @head: listint variable
 *
 * Return: int variable
 */

int is_palindrome(listint_t **head)
{
	int array[99999], i = 0, j = 0, ls_sz = 0;
	listint_t *aux;

	if (head == NULL || (*head) == NULL)
		return (1);
	aux = *head;
	while (aux != NULL)
	{
		array[i] = aux->n;
		aux = aux->next;
		i++;
	}
	i-=1;
	if (i % 2 != 0)
		ls_sz = (i + 1) / 2;
	else
		ls_sz = i / 2;
	while (j < ls_sz)
	{
		if (array[j] != array[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}

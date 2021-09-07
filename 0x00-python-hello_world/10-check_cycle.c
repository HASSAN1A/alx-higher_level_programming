#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga, *liebre;

	if (list == NULL || list->next == NULL)
		return (0);

	tortuga = list->next;
	liebre = list->next->next;

	while (tortuga && liebre && liebre->next)
	{
		if (tortuga == liebre)
			return (1);

		tortuga = tortuga->next;
		liebre = liebre->next->next;
	}

	return (0);
}
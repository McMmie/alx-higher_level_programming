#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted SLL
 * @head: points to the head pointer of the SLL
 * @number: value to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		tmp = *head = new;
		return (new);
	}

	tmp = *head;
	while (tmp->next != NULL)
	{
		prev = tmp;
		tmp = tmp->next;
		if (tmp->n < number)
		{
			continue;
		}
		else
		{
			new->next = tmp;
			prev->next = new;
			break;
		}
	}
	return (new);
}

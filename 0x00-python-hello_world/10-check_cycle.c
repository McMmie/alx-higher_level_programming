#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: points to a singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tail = list;
	listint_t *temp = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		if (temp->next != NULL && temp->next->next != NULL)
		{
			temp = temp->next->next;
			tail = tail->next;

			if (temp == tail)
			{
				return (1);
			}
		}
		else
		{
			return (0);
		}
	}
}

#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts node input list
 * at input's index (number)
 *
 * @head: Head of input list
 * @number: Index of insert
 *
 * Return: listing_t or null;
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new;
	int i;

	if (!*head)
	{
		add_nodeint_end(head, number);
		return (*head);
	}
	for (i = 0; temp && temp->next; temp = temp->next, i++)
	{
		if (number <= temp->next->n || !temp->next->next)
		{
			if (!temp->next->next && number > temp->next->n)
				temp = temp->next;
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			new->n = number;
			if (!i)
			{
				new->next = *head;
				*head = new;
			}
			else
			{
				new->next = temp->next;
				temp->next = new;
			}
			return (new);
		}
	}
	return (NULL);
}

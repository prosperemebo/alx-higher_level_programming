#include "lists.h"

/**
 * check_cycle - Checks if input list has cycle
 * @list: Input List
 *
 * Return: 0 on success
 */

int check_cycle(listint_t *list)
{
	listint_t *single, *doble;

	if (!list)
		return (0);

	for (single = doble = list; single && doble && doble->next;)
	{
		single = single->next;
		doble = doble->next->next;

		if (single == doble)
			return (1);
	}

	return (0);
}

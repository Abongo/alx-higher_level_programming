#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 *  Return: 1 if there is a cycle, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
	slow = slow->next;
	fast = fast->next->next;

	if (slow == fast)
	{
	return (1);
        }
	}
	return (0);
}


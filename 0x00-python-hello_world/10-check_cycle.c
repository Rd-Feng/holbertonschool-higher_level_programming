#include "lists.h"

/**
 * check_cycle - check if a list contains a loop
 * @list: head of list
 *
 * Return: 1 if loop exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list)
	{
		do {
			slow = slow->next;
			fast = fast->next;
			if (fast)
				fast = fast->next;
		} while (fast && slow != fast);
		if (slow == fast && fast)
			return (1);
	}
	return (0);
}

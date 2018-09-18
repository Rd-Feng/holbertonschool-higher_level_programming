#include "lists.h"
#include <stdlib.h>
int list_len(listint_t *);
/**
 * is_palindrome - check if a list is palindrome
 * @head: address of pointer to list
 *
 * Return: 0 if not, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int n = list_len(*head), arr[4096], half = n / 2, i;
	listint_t *ptr = NULL;

	if (!head)
		exit(-1);
	if (n > 1)
	{
		for (i = 0, ptr = *head; i < half; i++, ptr = ptr->next)
			arr[i] = ptr->n;
		if (n % 2)
			ptr = ptr->next;
		for (i = 0; i < half; i++, ptr = ptr->next)
			if (arr[half - i - 1] != ptr->n)
				return (0);
		return (1);
	}
	return (1);
}
/**
 * list_len - count number of nodes in a list
 * @head: head of list
 *
 * Return: number of nodes
 */
int list_len(listint_t *head)
{
	if (head)
		return (1 + list_len(head->next));
	return (0);
}

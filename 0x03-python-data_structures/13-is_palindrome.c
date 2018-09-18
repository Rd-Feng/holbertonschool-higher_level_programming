#include "lists.h"
#include <stdlib.h>
int list_len(listint_t *head);
listint_t *node(listint_t *head, int index);
int *list_to_arr(listint_t *head, int size);
/**
 * is_palindrome - check if a list is palindrome
 * @head: address of pointer to list
 *
 * Return: 0 if not, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int n = list_len(*head), *arr = NULL, half = n / 2;
	listint_t *ptr = NULL;

	if (!head)
		exit(-1);
	if (n > 1)
	{
		if (n % 2)
			arr = list_to_arr(node(*head, half + 1), half);
		else
			arr = list_to_arr(node(*head, half), half);
		if (!arr)
			exit(-1);
		for (n = 0, ptr = *head; n < half; n++, ptr = ptr->next)
			if (ptr->n != arr[half - n - 1])
			{
				free(arr);
				return (0);
			}
		free(arr);
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
/**
 * list_to_arr - convert a list into array
 * @head: head of list
 * @size: size of list
 *
 * Return: pointer to array, NULL on failure
 */
int *list_to_arr(listint_t *head, int size)
{
	int *arr = malloc(sizeof(int) * size);
	int i;

	if (arr)
		for (i = 0; i < size; i++, head = head->next)
			arr[i] = head->n;
	return (arr);
}
/**
 * node - get node at index
 * @head: head node
 * @index: index
 *
 * Return: node at index
 */
listint_t *node(listint_t *head, int index)
{
	while (index--)
		head = head->next;
	return (head);
}

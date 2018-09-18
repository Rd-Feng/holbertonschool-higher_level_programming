#include "lists.h"
#include <stdlib.h>
int list_len(listint_t *head);
int is_palin_arr(int *arr, int size);
int *list_to_arr(listint_t *head, int size);
/**
 * is_palindrome - check if a list is palindrome
 * @head: address of pointer to list
 *
 * Return: 0 if not, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int n = list_len(*head), *arr = NULL;

	if (!head)
		exit(-1);
	if (n > 1)
	{
		arr = list_to_arr(*head, n);
		if (!arr)
			exit(-1);
		n = is_palin_arr(arr, n);
		free(arr);
		return (n);
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
 * is_palin_arr - check if an array is palindrome
 * @arr: array
 * @size: array size
 *
 * Return: 0 if not, 1 otherwise
 */
int is_palin_arr(int *arr, int size)
{
	int i;

	for (i = 0; i < size / 2; i++)
		if (arr[i] != arr[size - i - 1])
			return (0);
	return (1);
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

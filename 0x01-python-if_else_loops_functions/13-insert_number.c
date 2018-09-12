#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: address of pointer to first node
 * @number: number to insert
 *
 * Return: pointer to inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p = NULL, *newNode = NULL;

	if (!head)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (newNode)
	{
		newNode->n = number;
		newNode->next = *head;
		if (!*head || newNode->n <= (*head)->n)
			*head = newNode;
		else
		{
			do {
				p = newNode->next;
				newNode->next = p->next;
			} while (newNode->next &&
				 newNode->n >= newNode->next->n);
			p->next = newNode;
		}
	}
	return (newNode);
}

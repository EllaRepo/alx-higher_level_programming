#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_nodeint - adds a new node at the beginning of a list_t list
 * @head: point to the pointer to the head of the list
 * @n: integer
 *
 * Return: the address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *node_ptr = malloc(sizeof(listint_t));

	if (!node_ptr)
		return (NULL);
	node_ptr->next = *head;
	node_ptr->n = n;
	*head = node_ptr;

	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: point to the head of listint_t list
 *
 * Return: 0 if it is not a palindrome
 *         1 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev_list = NULL, *h, *rh;

	if (*head == NULL || !(*head)->next ||
	((*head)->n == (*head)->n && !(*head)->next->next))
		return (1);
	for (h = *head; h; h = h->next)
		add_nodeint(&rev_list, h->n);
	for (h = *head, rh = rev_list; h; h = h->next, rh = rh->next)
	{
		if (h->n != rh->n)
		{
			free_listint(rev_list);
			return (0);
		}
	}
	free_listint(rev_list);
	return (1);
}

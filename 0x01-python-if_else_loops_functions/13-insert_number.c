#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: point to the head of listint_t list
 * @number: an integer to be added
 *
 * Return: the address of the new node
 *         NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **h = head, *new;

	if ((*h)->n > number || *h == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = number;
		new->next = (*h);
		*head = new;
		return (*head);
	}
	while (*h)
	{
		if ((*h)->n <= number && ((*h)->next->n >= number
			|| (*h)->next == NULL))
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			new->n = number;
			new->next = (*h)->next;
			(*h)->next = new;
			return (new);
		}
		*h = (*h)->next;
	}
	return (NULL);
}

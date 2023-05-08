#include "lists.h"

/**
 * free_listp - frees a listptr_t list
 * @head: pointer to list to be freed
 *
 * Return: void
 */
void free_listp(listptr_t *head)
{
	listptr_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
/**
 * add_listp_node - adds a new node at the beginning of a listptr_t list
 * @head: pointer to a pointer of the start of the list
 * @list: pointer to listint_t list be included in node
 *
 * Return: address of the new element or NULL if it fails
 */
listptr_t *add_listp_node(listptr_t **head, listint_t *list)
{
	listptr_t *new;

	new = malloc(sizeof(listptr_t));
	if (new == NULL)
		return (NULL);

	new->lptr = list;
	new->next = *head;
	*head = new;

	return (new);
}
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle
 *         1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listptr_t *listp = NULL, *tmp = NULL;

	while (list)
	{
		tmp = listp;
		while (tmp)
		{
			if (tmp->lptr == list)
			{
				free_listp(listp);
				return (1);
			}
			tmp = tmp->next;
		}
		add_listp_node(&listp, list);
		list = list->next;
	}
	if (listp)
		free_listp(listp);
	return (0);
}


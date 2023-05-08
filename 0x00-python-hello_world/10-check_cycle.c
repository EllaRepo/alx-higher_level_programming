#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle
 *         1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *list_ = list, *tmp;
	int i = 0;

	while (list_)
	{
		tmp = list;
		while (tmp)
		{
			if (tmp == list_)
				i += 1;
			if (i == 2)
				return (1);
			tmp = tmp->next;
		}
		i = 0;
		list_ = list_->next;
	}
	return (0);
}


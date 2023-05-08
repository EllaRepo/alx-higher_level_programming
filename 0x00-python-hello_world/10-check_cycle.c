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
	listint_t *list_, *tmp, *prev;

	list_ = tmp = prev = list;
	while (list_ && tmp && tmp->next)
	{
		list_ = list_->next;
		tmp = tmp->next->next;
		if (tmp == list_)
		{
			list_ = prev;
			prev =  tmp;
			while (1)
			{
				tmp = prev;
				while (tmp->next != list && tmp->next != prev)
					tmp = tmp->next;
				if (tmp->next == list_)
					break;
				list_ = list_->next;
			}
			return (1);
		}
	}
	return (0);
}



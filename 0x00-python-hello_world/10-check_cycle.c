#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop of cycle in it
 * @head: linked list to check
 * Return: 1 if the list has a loop or cycle, 0 otherwise
 */
int check_cycle(listint_t *head)
{
	listint_t *list1, *list2;

	list1 = head;
	list2 = head;
	while (list1 != NULL && list2 != NULL && list2->next != NULL)
	{
		list1 = list1->next;
		list2 = list2->next->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}

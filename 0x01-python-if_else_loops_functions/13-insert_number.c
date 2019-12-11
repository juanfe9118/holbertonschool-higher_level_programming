#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the linked list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *node_b4_ins = NULL, *node_af_ins = NULL;

	node_af_ins = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	if (number < node_af_ins->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	node_b4_ins = *head;
	node_af_ins = node_af_ins->next;

	while (number > node_af_ins->n)
	{
		node_b4_ins = node_b4_ins->next;
		node_af_ins = node_af_ins->next;
		if (node_af_ins == NULL)
			break;
	}
	new_node->next = node_b4_ins->next;
	node_b4_ins->next = new_node;
	return (new_node);
}

#include "lists.h"

/**
 * insert_node - inserts a node in linked list
 * @head: pointer to head of list
 * @number: the number to be added to new node
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *trav, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	trav = *head;
	if (number <= trav->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (number >= trav->next->n && trav->next)
	{
		trav = trav->next;
		if (trav->next == NULL && number < trav->n)
		{
			new_node = add_nodeint_end(head, number);
			if (!new_node)
				return (NULL);
			return (new_node);
		}
	}
	new_node->next = trav->next;
	trav->next = new_node;
	return (new_node);
}

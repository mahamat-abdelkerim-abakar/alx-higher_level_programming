#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function with two arguments
 * @head: head pointer to linked list
 * @number: input number
 *
 * Description: insert n value to sorted linked list
 * Return: address of new node, or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (new)
	{
		new->n = number;
		new->next = *head;
		if (new->next == NULL || new->n <= (*head)->n)
			*head = new;
		while(new->next && new->n > new->next->n)
		{
			prev = new->next;
			new->next = prev->next;
		}
		if (prev)
			prev->next = new;
	}

	return (new);
}

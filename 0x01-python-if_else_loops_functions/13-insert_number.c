#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: points to the head of the list
 * @number: data for new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *neow = NULL;

	if (!head)
		return (NULL);
	neow = malloc(sizeof(listint_t));
	if (neow == NULL)
		return (NULL);
	neow->n = number;
	neow->next = NULL;

	if (*head == NULL)
	{
		*head = neow;
		(*head)->next = NULL;
		return (neow);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < neow->n)
			(*head)->next = neow;
		else
		{
			neow->next = *head;
			*head = neow;
		}
		return (neow);
	}
	temp = *head;
	while (temp->next != NULL)
	{

		if (neow->n < temp->n)
		{
			neow->next = temp;
			*head = neow;
			return (neow);
		}

		if (((neow->n > temp->n) && (neow->n < (temp->next)->n)) ||
		    (neow->n == temp->n))
		{
			neow->next = temp->next;
			temp->next = neow;
			return (neow);
		}
		temp = temp->next;
	}
	temp->next = neow;
	return (neow);
}

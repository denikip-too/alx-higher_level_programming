#include "lists.h"

/**
 * print_listint - prints all the elements of a listint_t list
 * @h: variable pointer to the head of the list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	unsigned long int i;

	i = 0;
	while (h)
	{
		if (!h)
		{
			printf("[0] (nil)\n");
		}
		else
		{
			printf("%i\n", h->n);
		}
		h = h->next;
		i++;
	}
	return (i);
}

/**
 * *add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: variable pointer to the head of the list
 * @n: number of elements in a list
 * Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = n;
	new_node->next = (*head);
	(*head) = new_node;
	return (*head);
}

/**
 * free_listint - frees a listint_t list
 * @head: variable pointer to the head of the list
 */
void free_listint(listint_t *head)
{
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		free(current);
		current = next;
	}
	head = NULL;
}

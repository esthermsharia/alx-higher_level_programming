#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted linked list
 * @head: Pointer to a pointer pointing to the head node in a linked list
 * @number: Number to be inserted.
 *
 * Return: Pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **temp = head;
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *node2;

	new_node->n = number;
	if (new_node == NULL)
		return (NULL);



	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if ((*temp)->n >= number)
	{
		new_node->next = (*temp);
		*head = new_node;
		return (new_node);
	}

	while ((*temp) != NULL)
	{
		if (number >= (*temp)->n && number <= (*temp)->next->n)
		{
			node2 = (*temp)->next;
			(*temp)->next = new_node;
			new_node->next = node2;
			break;
		}
		(*temp) = (*temp)->next;
	}
	return (0);
}

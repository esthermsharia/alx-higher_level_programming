#include "lists.h"
/**
 * is_palindrome- Check if a singly linked list is a palindrome.
 * @head: pointer that points to a pointer that points to the
 *head of a linked list.
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int j = 0;
	int k = 0;
	int array[9999];

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	if (!temp->next)
		return (1);

	while (temp)
	{
		array[j] = temp->n;
		temp = temp->next;
		j++;
	}
	j--;
	while (j >= 0 && k <= j)
	{
		if (array[j] != array[k])
		{
			return (0);
		}
		j--;
		k++;
	}
	return (1);
}

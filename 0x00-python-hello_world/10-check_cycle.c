#include "lists.h"
/**
 * check_cycle - Checks availability of loop in a linked list
 * @list: Pointer to the actual list
 * Return: 0 if there is no cycle, 1 if there is a cyce
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	while (ptr1 != NULL && ptr1->next != NULL)
	{
		ptr2 = ptr2->next;
		ptr1 = ptr1->next->next;

		if (ptr1 == ptr2)
		{
			return (1);
		}
	}
	return (0);
}

#include "lists.h"
/**
 * check_cycle - checks for a loop in LL
 * @list: head of a linked list
 * Description - check for loop in LL
 * Return: 1 for cycled, 0 if not cycled
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if(!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

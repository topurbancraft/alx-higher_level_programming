#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
 * check_cycle - Function that checks the cycle of a serie of link-lists.
 * @list: argument of function.
 * Return: 1 if there is a cycle and 0 if there is no cycle.
 */

int check_cycle(listint_t *list)
{
listint_t *first = list, *last = list;

if (list != NULL)
{
while (first && first->next)
{
first = first->next->next;
last = last->next;
if (last == first)
{
first = list;
while (last != first)
{
last = last->next;
first = first->next;
}
return (1);
}
}
}
return (0);
}

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
} Node;

struct LinkedList {
    struct Node *head;

    void (*add)(struct LinkedList *self, int data);
    void (*print)(struct LinkedList *self);
    int (*size)(struct LinkedList *self);
    int (*search)(struct LinkedList *self, int data);
} LinkedList;

void add(struct LinkedList *self, int data) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;

    if (self->head == NULL) {
        self->head = node;
    } else {
        struct Node *current = self->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = node;
    }
}

void print(struct LinkedList *self) {
    struct Node *current = self->head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int search(struct LinkedList *self, int data) {
    struct Node *current = self->head;
    int index = 0;
    while (current != NULL) {
        if (current->data == data) {
            printf("Found %d at index %d\n", data, index);
            return index;
        }
        current = current->next;
        index++;
    }
    printf("%d not found\n", data);
    return -1;
}


int main(int argc, char const *argv[])
{
    struct LinkedList list;
    list.head = NULL;

    list.add = add;
    list.print = print;
    list.search = search;

    list.add(&list, 1);
    list.add(&list, 2);
    list.add(&list, 3);

    list.print(&list);

    list.add(&list, 4);

    list.print(&list);

    list.search(&list, 5);

    return 0;
}



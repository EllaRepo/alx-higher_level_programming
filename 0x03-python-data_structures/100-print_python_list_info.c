#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_list_info(PyObject *p)
{
	int size, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	size = Py_SIZE(list);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(list, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

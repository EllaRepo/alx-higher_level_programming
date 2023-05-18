#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_bytes(PyObject *p)
{
	char *string, c;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	limit = size >= 10 ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		c = string[i] >= 0 ? string[i] : string[i] + 256;
		printf(" %02x", c);
	}
	printf("\n");
}
/**
 * print_python_list - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

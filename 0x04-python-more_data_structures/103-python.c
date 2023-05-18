#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	char *buffer;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	buffer = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);

	size = = size > 10 ? 10 : size + 1;

	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		if (buffer[i] >= 0)
			printf(" %02x", buffer[i]);
		else
			printf(" %02x", buffer[i] + 0xFF4);
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
	Py_ssize_t size = 0, i = 0;
	PyObject *item;
	const char *type_name;

	size = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
		if (PyBytes_Check(obj))
			print_python_bytes(item);
	}
}

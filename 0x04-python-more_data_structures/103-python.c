#include <Python.h>

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

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size = PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	unsigned char *buffer;
	Py_ssize_t size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	buffer = (unsigned char *)bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);

	if (size > 10)
		size = 10;
	printf("  first %ld bytes:", size);
	for (Py_ssize_t i = 0; i < size; i++)
		printf(" %02x", buffer[i]);
	printf("\n");
}

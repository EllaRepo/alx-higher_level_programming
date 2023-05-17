#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: points to an object of type PyObject
 *
 * Return: None
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	PyTypeObject *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %ld: %s\n", i, type->tp_name);
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
	buffer = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);

	if (size > 10)
		size = 10;
	printf("  first %ld bytes:", size);
	for (Py_ssize_t i = 0; i < size; i++)
		printf(" %02x", buffer[i]);
	printf("\n");
}

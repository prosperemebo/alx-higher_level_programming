#include <Python.h>

/**
 * print_python_bytes - Prints input python bytes
 *
 * @p: byte
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *trying_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &trying_str, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %ld bytes:", ++size);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_list - Prints input python lists
 *
 * @p: list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	int i;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		type = (((PyListObject *)p)->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}

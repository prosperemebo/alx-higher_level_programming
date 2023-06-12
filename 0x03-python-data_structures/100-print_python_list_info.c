#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints python list info
 * @p: list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	PyObject *item;
	int i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

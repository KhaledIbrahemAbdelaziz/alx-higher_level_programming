#include <Python.h>

/**
 * print_python_list_info - prints some basic info
 * about Python lists.
 * @p: A PyObject list.
 * Return: nothing to return.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	print("[*] Size of the Python List = %d\n", size);
	print("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		print("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

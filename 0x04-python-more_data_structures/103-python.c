#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes: ", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; ++i)
	printf("%02x%c", string[i] & 0xFF, (i == size - 1 || i == 9) ? '\n' : ' ');
}

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	if (PyBytes_Check(item))
	print_python_bytes(item);
	}
}

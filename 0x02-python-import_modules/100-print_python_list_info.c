#include <Python.h>
#include <stdio.h>
#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

        printf("[*] Size of the Python List = %zd\n", Py_SIZE(p));
        printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < Py_SIZE(p); i++)
	{
                printf("Element %zd: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

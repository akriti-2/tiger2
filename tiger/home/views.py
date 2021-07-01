from django.shortcuts import render
from tests.forms import CommandForm
import subprocess as sp

# Create your views here.
def home(request):
    return render(request, 'index.html')

def result(request):
    output = ""
    myform = CommandForm()

    if request.method == "POST":
        myform = CommandForm(request.POST)
        if myform.is_valid():
            execute_command = myform.cleaned_data['command']
            try:
                output = sp.check_output(execute_command, shell=True)
            except sp.CalledProcessError:
                exit_code, error_msg = output.returncode, output.output
    return render(request, 'result.html', locals())


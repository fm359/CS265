cc = gcc
EXE = foo
JAVAC = javac
JRE = java
PAGER = less
TEST_OUT = test.out
EXP_OUT = expected.out

foo.o : foo.c foo.h
	$(cc) -c foo.c foo.h

main.o : main.c foo.h
	$(cc) -c main.c foo.h

$(EXE) : foo.o main.o
	$(cc) -o$(EXE) main.o foo.o

run-c: $(EXE)
	./$(EXE)

run-py: foo.py
	./foo.py

read:
	$(PAGER) README

foo.class: foo.java
	$(JAVAC) foo.java

run-java: foo.class
	$(JRE) foo

save-java:
	 $(JRE) foo > $(TEST_OUT)

test-java:
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null ; then \
	    echo "Passed!" ;\
	else \
  	    echo "Not the same!" ;\
	fi

.PHONY : clean
clean :
	-\rm *.o
	-\rm $(EXE)
	-\rm run-c
	-\rm run-py
	-\rm foo.class
	-\rm run-java
	-\rm save-java
	-\rm test.java

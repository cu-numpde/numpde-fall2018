# Numerical solution of partial differential equations

## Syllabus

CU Boulder: CSCI 5636-001(B) (Fall 2018)

Meeting Time: MWF 2:00-2:50pm in ECCR 1B51

#### Remote access via Zoom

* Join via web browser: https://cuboulder.zoom.us/j/593324843
* Join via Zoom app (using meeting ID 593-324-843)
* Join via phone: +1-669-900-6833 or +1-646-558-8656

#### Recordings

* https://cu-classcapture.colorado.edu/Mediasite/Catalog/Full/b6950dea3ec743eca009777dd486fa5e21

#### Gitter discussion forum

https://gitter.im/cucs-numpde/Lobby

#### Instructor

[Jed Brown](https://jedbrown.org), [<tt>jed.brown@colorado.edu</tt>](mailto:jed.brown@colorado.edu), ECOT 621

Office Hours: Mon 9-10am, Thu 8:30-10am, or by appointment.

### Overview

Partial differential equations (PDE) describe the behavior of fluids, structures, heat transfer, wave propagation, and other physical phenomena of scientific and engineering interest.  This course 
covers discretization of PDE using finite difference and collocation methods, finite volume methods, and finite element methods for elliptic, parabolic, and hyperbolic equations.  We will discuss foundational principles like will posedness and explores efficient methods for solution of the discretized equations.

### Organization

We will start with a brief refresher on numerical integration, approximation of functions, and numerical differentiation.  We will extend this to finite difference methods for elliptic problems (like heat and pressure equilibrium) and time integration, producing methods that converge with arbitrarily high orders of accuracy.  We will discover challenges when applying these methods to hyperbolic equations (which describe wave propagation and transport phenomena), especially nonlinear hyperbolic equations, and thus develop finite volume methods which rely on weaker assumptions.  We will learn about shocks, rarefactions, and Riemann solvers.  Finite volume methods are easy to use in complicated geometries and/or unstructured meshes, but achieving high order accuracy in such settings is unnatural and the methods can be awkward for elliptic and parabolic equations.  Finite element methods offer a flexible and robust analysis framework as well as modular implementation that allows arbitrary order of accuracy even in complicated domains.  We will introduce relevant concepts in continuum mechanics as we go.

### Benefits

Partial differential equations underly a broad range of high-fidelity models in science and engineering from atomic to cosmological scales.
Upon completing this course, students possess an ability to

* formulate problems in science and engineering in terms of partial differential equations
* understand the merits and limitations of the leading numerical methods used to solve PDE
* recognize and exploit structure to apply algorithms that improve performance and scalability
* select and use robust software libraries
* develop effective numerical software, taking into account stability, accuracy, and cost
* predict scaling challenges and computational costs when solving increasingly complex problems or attempting to meet real-time requirements
* interpret research papers and begin research in the field

### Evaluation

* 40% class participation and contribution to homework, which will involve some software development and numerical experiments.
* 30% final project.  A one-page written proposal is due November 12 and the project (code + write-up) is due on December 18.  I'll help you find a suitable project.
* Two open-neighbor midterms of 15% each, to be held in-class October 5 and November 9.

Assignments will be submitted via GitHub.  Start by forking the [class repository](https://github.com/cucs-numpde/numpde).

The grade for coding assignments will be a combination of pure correctness, code quality, and efficiency/scalability. It is notoriously difficult to predict the time required to produce quality code, so please start early to give yourself plenty of time.

You are encouraged to work together on all assignments, but must give credit to peer contributions via the commit messages or Git history. For example, you would add

    Suggested-by: Friendly Neighbor <friendly.neighbor@colorado.edu>

to the commit message if that code incorporates an approach suggested by your neighbor.  Alternatively, you can `merge` or `cherry-pick` a commit written by your peer (these operations preserve author information). You should ensure that each assignment (pull request) contains some of your own meaningful intellectual contributions.

### Programming languages and environment

I will use Python and [Jupyter notebooks](https://jupyter.org/) for most examples in class.  This environment is convenient to work with, general purpose, and has extensive library support.  Native Python code is not high performance, however.  Production numerical software is most frequently written in C, C++, or Fortran, perhaps called from a higher level programming language like Python.  MATLAB is also popular for numerical computing, though it is a proprietary environment and lacks general-purpose libraries.  Octave is a free MATLAB clone and Julia is a modern language that preserves much of the syntactic convenience.  Any language is allowed for your own work, but I recommend one of the above.  Most HPC facilities use a Linux operating system.  You can use any environment for your local development environment, or use [Azure notebooks](https://notebooks.azure.com/) to experiment and develop in the cloud (sign in with colorado.edu credentials).

### Target audience

Graduate students in computer science or simulation-based science or engineering.  Suggested prereq: at least one of

* CSCI-2820 Linear Algebra
* CSCI-3656 Numerical Computation
* CSCI-4576 High-Performance Scientific Computing

### Resources (updated continuously)

* http://www.siam.org/students/memberships.php (SIAM Membership is free for CU students, 30% discount on SIAM books)
* [LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*](https://faculty.washington.edu/rjl/fdmbook/) (CU students can [download free from SIAM](http://epubs.siam.org/doi/book/10.1137/1.9780898717839))
* [LeVeque, *Finite Volume Methods for Hyperbolic Problems*](https://depts.washington.edu/clawpack/book.html) and the [Clawpack software](http://www.clawpack.org/).
* [Toro, *Riemann Solvers and Numerical Methods for Fluid Dynamics*](https://link.springer.com/book/10.1007%2Fb79761#toc). (CU students can download free)
* [Logg, Mardal, Wells, *Automated Solution of Differential Equations by the Finite Element Method (The FEniCS Book)*](https://link.springer.com/book/10.1007%2F978-3-642-23099-8). (free download)
* [Trefethen, *Spectral Methods in MATLAB*](https://people.maths.ox.ac.uk/trefethen/spectral.html). (CU students can [download free from SIAM](http://epubs.siam.org/doi/book/10.1137/1.9780898719598))
* Elman, Silvester, Wathen, *Finite Elements and Fast Iterative Solvers with Applications in Incompressible Fluid Dynamics*

### Disability Accommodations

If you qualify for accommodations because of a disability, please submit to your professor a letter from Disability Services in a timely manner (for exam accommodations provide your letter at least one week prior to the exam) so that your needs can be addressed. Disability Services determines accommodations based on documented disabilities. Contact Disability Services at 303-492-8671 or by e-mail at dsinfo@colorado.edu. If you have a temporary medical condition or injury, see the Temporary Injuries guidelines under the Quick Links at the Disability Services website and discuss your needs with your professor.

### Religious Observances

[Campus policy regarding religious observances](http://www.colorado.edu/policies/fac_relig.html) requires that faculty make every effort to deal reasonably and fairly with all students who, because of religious obligations, have conflicts with scheduled exams, assignments or required assignments/attendance. If this applies to you, please speak with me directly as soon as possible at the beginning of the term. See the [campus policy regarding religious observances](http://www.colorado.edu/policies/observance-religious-holidays-and-absences-classes-andor-exams) for full details.

### Classroom Behavior

Students and faculty each have responsibility for maintaining an appropriate learning environment. Those who fail to adhere to such behavioral standards may be subject to discipline. Professional courtesy and sensitivity are especially important with respect to individuals and topics dealing with differences of race, color, culture, religion, creed, politics, veteran's status, sexual orientation, gender, gender identity and gender expression, age, disability,and nationalities. Class rosters are provided to the instructor with the student's legal name. I will gladly honor your request to address you by an alternate name or gender pronoun. Please advise me of this preference early in the semester so that I may make appropriate changes to my records. For more information, see the policies on [classroom behavior](http://www.colorado.edu/policies/student-classroom-and-course-related-behavior) and the [student code](http://www.colorado.edu/osc/sites/default/files/attached-files/studentconductcode_16-17-a.pdf).

### Discrimination and Harassment

The University of Colorado Boulder (CU Boulder) is committed to maintaining a positive learning, working, and living environment. CU Boulder will not tolerate acts of sexual misconduct, discrimination, harassment or related retaliation against or by any employee or student. CU's Sexual Misconduct Policy prohibits sexual assault, sexual exploitation, sexual harassment,intimate partner abuse (dating or domestic violence), stalking or related retaliation. CU Boulder's Discrimination and Harassment Policy prohibits discrimination, harassment or related retaliation based on race, color,national origin, sex, pregnancy, age, disability, creed, religion, sexual orientation, gender identity, gender expression, veteran status, political affiliation or political philosophy. Individuals who believe they have been subject to misconduct under either policy should contact the Office of Institutional Equity and Compliance (OIEC) at 303-492-2127. Information about the OIEC, the above referenced policies, and the campus resources available to assist individuals regarding sexual misconduct, discrimination, harassment or related retaliation can be found at the [OIEC website](http://www.colorado.edu/institutionalequity/).

### Honor Code

All students enrolled in a University of Colorado Boulder course are responsible for knowing and adhering to the [academic integrity policy](http://www.colorado.edu/policies/academic-integrity-policy) of the institution. Violations of the policy may include: plagiarism, cheating,fabrication, lying, bribery, threat, unauthorized access, clicker fraud,resubmission, and aiding academic dishonesty.  All incidents of academic misconduct will be reported to the Honor Code Council (honor@colorado.edu; 303-735-2273). Students who are found responsible for violating the academic integrity policy will be subject to nonacademic sanctions from the Honor Code Council as well as academic sanctions from the faculty member. Additional information regarding the academic integrity policy can be found at http://honorcode.colorado.edu.

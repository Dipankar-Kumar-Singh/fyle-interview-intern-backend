from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.apis.teachers.schema import TeacherSchema
from core.libs import assertions
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.teachers import Teacher

from core.apis.assignments.schema import AssignmentSchema ,AssignmentGradeSchema
principal_resources = Blueprint('principal_resources', __name__)


@principal_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns List all submitted and graded assignments""" 
    assignments = Assignment.get_non_draft_assignments() ;
    assignments_dump = AssignmentSchema().dump(assignments, many=True) 
    return APIResponse.respond(data=assignments_dump)
    

@principal_resources.route("/teachers" , methods=['GET'], strict_slashes = False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of all the teachers"""
    teachers = Teacher.get_all() ;
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump);


@principal_resources.route('assignments/grade' , methods=['POST'] , strict_slashes = False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p,incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload) ;
    assignment = Assignment.get_by_id(grade_assignment_payload.id) ;

    graded_assignment = Assignment.mark_grade(
         _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit() ;
    grade_assignment_dump = AssignmentSchema().dump(graded_assignment) ;
    return APIResponse.respond(data=grade_assignment_dump)
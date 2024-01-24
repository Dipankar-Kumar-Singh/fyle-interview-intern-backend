from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentSubmitSchema
principal_resources = Blueprint('principal_resources', __name__)


@principal_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns List all submitted and graded assignments""" 
    assignments = Assignment.get_all() ;
    assignments_dump = AssignmentSchema().dump(assignments, many=True) 
    return APIResponse.respond(data=assignments_dump)
    

# @principal_resources.route("/teachers" , methods=['GET'], strict_slashes = False)
# @decorators.authenticate_principal
# def list_teachers(p):



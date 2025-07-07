/** @odoo-module */
import { FormController } from "@web/views/form/form_controller";
import { formView } from '@web/views/form/form_view';
import { registry } from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";

export class StudentFormController extends FormController {
    setup() {
        super.setup();
        this.actionService = useService("action");

    }

    OnTestClick() {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'student.student',
            name: 'Open Wizard',
            view_mode: 'form',
            view_type: 'form',
            views: [[false, 'form']],
            target: 'new',
            res_id: false,
        });
    }
}
StudentFormController.template = 'button_Student.FormView.Buttons';
export const modelInfoView = { ...formView, Controller: StudentFormController, };
registry.category("views").add("button_in_form", modelInfoView);
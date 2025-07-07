/** @odoo-module */
import { registry } from '@web/core/registry';
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
export class studentKanbanController extends KanbanController {
   setup() {
       super.setup();
   }
   OnTestClick() {
       this.actionService.doAction({
          type: 'ir.actions.act_window',
          res_model: 'student.student',
          name:'Open Wizard',
          view_mode: 'form',
          view_type: 'form',
          views: [[false, 'form']],
          target: 'new',
          res_id: false,
      });
   }
}
studentKanbanController.template = "module.kanban.Buttons";
export const customstudentKanbanController = {
    ...kanbanView,
    Controller: studentKanbanController,
};
registry.category("views").add("button_in_kanban", customstudentKanbanController);

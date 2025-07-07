/** @odoo-module */
import { registry } from '@web/core/registry';
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
export class productKanbanController extends KanbanController {
   setup() {
       super.setup();
   }
   OnTestClick() {
       this.actionService.doAction({
          type: 'ir.actions.act_window',
          res_model: 'product.template',
          name:'Open Wizard',
          view_mode: 'form',
          view_type: 'form',
          views: [[false, 'form']],
          target: 'new',
          res_id: false,
      });
   }
}
productKanbanController.template = "module.kanban.Buttons.product";
export const customproductKanbanController = {
    ...kanbanView,
    Controller: productKanbanController,
};
registry.category("views").add("button_in_kanban_product", customproductKanbanController);

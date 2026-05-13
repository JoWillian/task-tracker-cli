import datetime

from storage import save_tasks, load_tasks
import argparse


def main():
    parser = argparse.ArgumentParser('Task Tracker')
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add task')
    add_parser.add_argument('description', help='The description of the task')

    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    mark_done_parser.add_argument('id', type=int, help='The id of the task you want to mark as done')

    mark_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task in-progress')
    mark_progress_parser.add_argument('id', type=int, help='The id of the task you want to mark in-progress')

    delete_parser= subparsers.add_parser('delete', help='Delete task')
    delete_parser.add_argument('id', type=int, help='The id of the task you want to delete')

    update_parser = subparsers.add_parser('update', help='Update task')
    update_parser.add_argument('id', type=int, help='The id of the task you want to update')
    update_parser.add_argument('description', help='The description of the task you want to update')


    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status',nargs='?', type=str, help='The status of the task you want to list')

    args = parser.parse_args()

    if args.command == 'add':

        tasks = load_tasks()

        new_task = {
            'id': max([task['id'] for task in tasks], default=0) + 1 ,
            'description': args.description,
            'status': 'todo',
            'createdAt': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'updatedAt': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }

        tasks.append(new_task)
        save_tasks(tasks)

        print(f"Task added successfully (ID: {new_task['id']})")

    elif args.command == 'mark-done':
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == args.id:
                task['status'] = "done"
                task['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f'marking task ID ({args.id}) as done.')
                break

        save_tasks(tasks)

    elif args.command == 'mark-in-progress':
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == args.id:
                task['status'] = "in-progress"
                task['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f'marking task ID ({args.id}) as in-progress.')
                break

        save_tasks(tasks)

    elif args.command == 'delete':
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == args.id:
                tasks.remove(task)
                break

        save_tasks(tasks)
        print(f'Task deleted: {args.id}')

    elif args.command == 'update':
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == args.id:
                task['description'] = args.description
                task['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f'Updating task ID ({args.id}) to {args.description}')
                break

        save_tasks(tasks)

    elif args.command == 'list':
        tasks = load_tasks()
        for task in tasks:
            # Logic: If user didn't provide a status OR the status matches...
            if not args.status or task['status'] == args.status:
                print(f"{task['id']}: {task['description']} [{task['status']}] - Created at {task['createdAt']}")

if __name__ == '__main__':
    main()
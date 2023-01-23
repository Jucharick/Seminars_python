import view
import model



def start():
    value =''
    while value !=8:
        value = view.menu()
        match value:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_contact())
                model.add_new_contact(new_contact)
            case 5:
                model.del_contact()
            case 6:
                model.update_contact()
                
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                model.exit_phone_book()
            case _: # работает как else
                view.input_err()
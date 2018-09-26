//
//  address_type_range.cpp
//  blocksci_interface
//
//  Created by Harry Kalodner on 11/19/17.
//

#include "optional_ranges_py.hpp"
#include "caster_py.hpp"

#include <blocksci/chain/block.hpp>
#include <blocksci/cluster/cluster.hpp>

namespace py = pybind11;
using namespace blocksci;

void init_address_type_range(py::module &m) {
    constexpr auto rangeCat = ranges::category::random_access | ranges::category::sized;
    {
        py::class_<ranges::any_view<ranges::optional<AddressType::Enum>>> cl(m, "AddressTypeOptionalIterator");
        addOptionalRangeMethods(cl);
    }
    {
        py::class_<ranges::any_view<ranges::optional<AddressType::Enum>, rangeCat>> cl(m, "AddressTypeOptionalRange");
        addOptionalRangeMethods(cl);
    }
}